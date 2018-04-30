
import re

from PyQt5.QtCore import Qt
from PyQt5.QtGui import (
    QCursor,
    QFont,
)
from PyQt5.QtWidgets import (
    QAction,
    QFontDialog,
    QMenu,
)

from collections import namedtuple

from plover.formatting import RetroFormatter
from plover.misc import shorten_path
from plover_advanced_lookup.advanced_lookup_ui import Ui_AdvancedLookup
from plover.gui_qt.i18n import get_gettext
from plover.gui_qt.utils import ToolBar
from plover.gui_qt.tool import Tool


_ = get_gettext()

StenoEntry = namedtuple('StenoEntry', ['steno', 'translation', 'num_strokes', 'dictionary', 'dictionary_index'])

class AdvancedLookup(Tool, Ui_AdvancedLookup):

    ''' Suggest possible strokes for the last written words. '''

    TITLE = _('Advanced Lookup')
    ICON = ':/lightbulb.svg'
    ROLE = 'advanced_lookup'
    SHORTCUT = 'Ctrl+Shift+L'

    CUT_OFF = 50


    WORD_RX = re.compile(r'(?:\w+|[^\w\s]+)\s*')

    STYLE_TRANSLATION, STYLE_STROKES = range(2)

    # Anatomy of the text document:
    # - "root" frame:
    #  - 0+ "suggestions" frames
    #   - 1+ "translation" frames
    #    - 1-10 "strokes" frames

    def __init__(self, engine):
        super().__init__(engine)
        self.setupUi(self)
        self._last_search = None
        # Toolbar.
        self.layout().addWidget(ToolBar(
            self.action_ToggleOnTop,
            self.action_SelectFont,
            self.action_Clear,
        ))
        self.action_Clear.setEnabled(False)
        # Font popup menu.
        self._font_menu = QMenu()
        self._font_menu_text = QAction(_('&Text'), self._font_menu)
        self._font_menu_strokes = QAction(_('&Strokes'), self._font_menu)
        self._font_menu.addActions([self._font_menu_text, self._font_menu_strokes])
        self.searchInput.setFocus()
        self.restore_state()
        self.finished.connect(self.save_state)

    def _get_font(self, name):
        return getattr(self.byTranslationText, name)

    def _set_font(self, name, font):
        setattr(self.byTranslationText, name, font)
        setattr(self.inTranslationText, name, font)
        setattr(self.byStrokeText, name, font)
        setattr(self.inStrokeText, name, font)

    def _restore_state(self, settings):
        for name in (
            'text_font',
            'strokes_font',
        ):
            font_string = settings.value(name)
            if font_string is None:
                continue
            font = QFont()
            if not font.fromString(font_string):
                continue
            self._set_font(name, font)
        ontop = settings.value('ontop', None, bool)
        if ontop is not None:
            self.action_ToggleOnTop.setChecked(ontop)
            self.on_toggle_ontop(ontop)

    def _save_state(self, settings):
        for name in (
            'text_font',
            'strokes_font',
        ):
            font = self._get_font(name)
            font_string = font.toString()
            settings.setValue(name, font_string)
        ontop = bool(self.windowFlags() & Qt.WindowStaysOnTopHint)
        settings.setValue('ontop', ontop)

    def _results_to_string(self, results, translation_first = False):
        current_dictionary_index = None
        display_strings = []
        for (steno, translation, num_stroke, dictionary, dictionary_index) in results:
            if current_dictionary_index != dictionary_index:
                current_dictionary_index = dictionary_index
                display_strings.append(shorten_path(dictionary.path))
            if translation_first:
                display_strings.append('  ' + translation + ': ' + steno)
            else:
                display_strings.append('  ' + steno + ': ' + translation)
        return '\n'.join(display_strings)

    def on_lookup(self, search):
        search = search.strip()
        if not search:
            self.on_clear()
            return
        isearch = search.lower()
        translation_starts_with = []
        translation_inside = []
        steno_starts_with = []
        steno_inside = []
        dictionary_index = 0
        for dictionary in self._engine.dictionaries.dicts:
            for strokes, translation in dictionary.items():
                steno = '/'.join(strokes)
                num_strokes = len(strokes)
                itranslation = translation.lower()
                result = StenoEntry(steno, translation, num_strokes, dictionary, dictionary_index)
                if (steno + '/').startswith(search):
                    steno_starts_with.append(result)
                elif search in ('/' + steno + '/'):
                    steno_inside.append(result)

                if itranslation.startswith(isearch):
                    translation_starts_with.append(result)
                elif isearch in itranslation:
                    translation_inside.append(result)
            dictionary_index += 1
        print(len(translation_starts_with), len(translation_inside), len(steno_starts_with), len(steno_inside))

        def suggestion_key(entry):
            return (entry.dictionary_index, entry.num_strokes, len(entry.translation), len(entry.steno))

        translation_starts_with.sort(key=suggestion_key)
        for result in (translation_starts_with, translation_inside, steno_starts_with, steno_inside):
            result.sort(key=suggestion_key)

        self.byStrokeText.setPlainText(self._results_to_string(steno_starts_with))
        self.inStrokeText.setPlainText(self._results_to_string(steno_inside))
        self.byTranslationText.setPlainText(self._results_to_string(translation_starts_with, True))
        self.inTranslationText.setPlainText(self._results_to_string(translation_inside, True))

        self.action_Clear.setEnabled(True)
        return

    def on_select_font(self):
        action = self._font_menu.exec_(QCursor.pos())
        if action is None:
            return
        if action == self._font_menu_text:
            name = 'text_font'
            font_options = ()
        elif action == self._font_menu_strokes:
            name = 'strokes_font'
            font_options = (QFontDialog.MonospacedFonts,)
        font = self._get_font(name)
        font, ok = QFontDialog.getFont(font, self, '', *font_options)
        if ok:
            self._set_font(name, font)

    def on_toggle_ontop(self, ontop):
        flags = self.windowFlags()
        if ontop:
            flags |= Qt.WindowStaysOnTopHint
        else:
            flags &= ~Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)
        self.show()

    def on_clear(self):
        self.action_Clear.setEnabled(False)
        self._last_search = None
        self.searchInput.clear()
        self.byStrokeText.clear()
        self.inStrokeText.clear()
        self.inTranslationText.clear()
        self.byTranslationText.clear()
        self.searchInput.setFocus()
