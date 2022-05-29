
# Description of the parameters and settings file.

___

<!-- Data Types. -->
[^text]: A text data type. A value escaped by quotation marks is expected.
[^bool]: Boolean data type. true/false.
[^positive]: Positive numeric data type. A number from a set of positive real numbers is expected.

[^GUI]: Graphical User Interface. The setting window that shows up in the game.
[^inSettingMenu]: Parameter name in the GUI.

## Example of a setting file:

```json
{
    "gameLanguage": "ja",
    "directionOfTranslation": "en",
    "prescanOnStartup": false,
    "realtimeTranslationOnStartup": false,
    "_debug_mode": false,
    "translationService": "selenium_deepl",
    "workMethod": "dialogueOnly",
    "originalInHistory": false,
    "requestsFrequency": null,
    "splitTextAsSentences": false,
    "googleHost": "translate.google.com",
    "seleniumStartMode": "hide",
    "seleniumInputSplitMethod": "strings",
    "extraTextOptions": {
        "font": null,
        "size": null,
        "italic": false,
        "bold": false
    }
}
```

___

* The format of the description is as follows:
    * First the name of the parameter in the configuration file is specified.
        * On the same line there is a number-note of the allowed data type.
            * A text data type: [^text]
                * A value escaped by quotation marks is expected.
            * Boolean data type: [^bool]
                *  ___true___ / ___false___
            * Positive numeric data type: [^positive]
                * A number from a set of positive real numbers is expected.
    * The next line contains the name of the corresponding item in the GUI[^GUI].
        * Only if there is one, as there are parameters that are not available in the GUI[^GUI].
    * This is followed by an explanation of the specifics of the item.

___

* The following terms may appear in the text: ___prescan___, ___real-time translation___, and so on. Information about them can be found in the corresponding sections of the [FAQ](../FAQ/EN.md).

* If there are settings in this documentation that are not yet in the translator, you should ignore them, because the documentation is being written at the same time as the update of the translator and, at the moment, these items are still in beta-test.

___

* ### Disclamer:

    1. The information provided in this documentation is for informational purposes only.
    1. It is better to make all necessary settings in the GUI[^GUI].
    1. It is highly recommended not to change anything in the configuration file, without a full understanding of your actions.
    1. The creator of the translator does not take any responsibility for the incorrect work, if you manually change the settings file.

___

## Parameter Description.

1. ###  ___gameLanguage___: [^text]
    * __"The original language of the game."__ [^inSettingMenu]

    * The language of the game itself (from which you need a translation).
        * Language code from a specific service, or the name of the language in English.
            * Examples of valid parameters:
                *  "en"
                *  "en-GB"
                *  "Portuguese"
                *  "Polish"
                *  "Chinese"


1. ### ___directionOfTranslation___: [^text]

    * __"Direction of translation."__ [^inSettingMenu]

    * The language in which to translate the game.
        * The format of the specified data is identical to parameter ___gameLanguage___.


1. ### ___prescanOnStartup___: [^bool]

    * __"Prescan at the start of the game."__ [^inSettingMenu]

    * When this option is activated, it starts a prescan at the moment the game starts.
    * Not recommended for use except in special situations, as it is very time-consuming if the game has an initial splash screen, etc.


1. ### ___realtimeTranslationOnStartup___: [^bool]

    * __"Realtime translation at the start of the game."__ [^inSettingMenu]

    * When this option is activated, it starts a real-time translation when the game starts.
    * Just as in the previous paragraph, it is not recommended for use, except in special situations, for the same reasons.


1. ### ___\_debug_mode___: [^bool]

    * __"Debug mode."__ [^inSettingMenu]

    * When this option is activated, translator work changes as follows:
        * If an error occurs, traceback will be raised.
        * Logging of the translator's actions will be enabled.
    * Except in special cases, you should not activate this option.


1. ### ___translationService___: [^text]

    * __"Translation service."__ [^inSettingMenu]

    * The service that will do the translation.
    * The following values are valid:

        * __*"google_gtx"*__:

            * __Non-browser logic.__
            * The service with the best (among non-browser) translation quality.
            * Since Google bans on suspicion of automation, the request frequency is forcibly reduced to 8 requests per minute.

        * __*"google_client5"*__:

            * __Non-browser logic.__
            * A service with poor translation quality but good speed.

        * __*"google_rpc"*__:

            * __Non-browser logic.__
            * Completely identical to ___"google_client5"___, but with the ability to change the service host (parameter ___"googleHost"___).

        * __*"selenium_deepl"*__:

            * __Browser logic.__
            * Service with the best, among the presented, translation quality.
            * There are disadvantages, typical for translators with browser logic.
                * You can read more in the relevant section in the [FAQ](../FAQ/EN.md#about-browser-logic).


1. ### ___workMethod___: [^text]

    * __"Method of work of the translator."__ [^inSettingMenu]

    * Translator's work method.
    * The following values are valid:

        * ___"dialogueOnly"___:
            * __"Translation of dialogs and choice menus."__ [^inSettingMenu]
            * Translator will use parameter [__config.say_menu_text_filter__](https://www.renpy.org/doc/html/config.html#var-config.say_menu_text_filter) to work.
            * The main text (in the dialog box) and the choice menu will be translated.
            * In most cases it is recommended to use this parameter.

        * ___"allText"___:
            * __"Translation of all text in the game (Beta)."__ [^inSettingMenu]
            * Translator will overwrite the built-in [__Text.set_text__](https://github.com/renpy/renpy/blob/df628ea0f54c434d790a7e7527a47efc16092e41/renpy/text/text.py#L1672) method.
            * All displayed text on the screen will be translated.
            * The mode is in beta stage and is not recommended for use unless absolutely necessary.
            * Since when this option is activated all the text on the screen will be translated, it is possible long "freeze" in the game.
            * Absolutely contraindicated for use if the game demonstrates dynamic data.
                * Such as:
                    * _Time._
                    * _Changing a character's stats._
                    * _etc._
                * Because the translator will try to translate each of the new values, which will cause the process to freeze completely.


1. ### ___originalInHistory___: [^bool]

    * __"Save the original text in the history."__ [^inSettingMenu]

    * If this option is enabled, the ["history" screen](https://www.renpy.org/doc/html/history.html#dialogue-history) will display the original text instead of the translation.


1. ### ___requestsFrequency___: [^positive]

    * __"Frequency of requests."__ [^inSettingMenu]

    * Frequency of requests to the translation service.
        * Number of requests per minute.
    * For some translation services, the value is fixed and unchangeable.
    * For services with browser logic the value is ignored.


1. ### ___splitTextAsSentences___: [^bool]

    * __"Split sentences during translation."__ [^inSettingMenu]

    * If this option is activated, the text will be divided into "sentences" according to the following [pattern](https://docs.python.org/2.7/library/re.html) before translation:

        ```python
        # Python RE logic.
        r"(?P<text>[^!?….\r\n]+)(?P<end_mark>[!?….]*)"
        ```

    * Some translation services (e.g. __*google_client5*__) return an incorrect translation if there are excessive punctuation marks in the text. This setting prevents this from happening.
    * In some services, this parameter is activated by default and a user value is ignored (for example, in the previously mentioned service __*google_client5*__).
    * It is not recommended to activate this option.
        * In those services where it is required, it is activated by default.


1. ### ___googleHost___: [^text]

    * Host for translation service __*google_rpc*__.
        * __When selecting other services, this option will be ignored.__
    * For countries where the standard ___translate.google.com___ does not work correctly (or slowly).
    * For example:
        * For Latvia:
            * ___"translate.google.lv"___
        * For China:
            * ___"translate.google.cn"___
        * And so on.


1. ### ___seleniumStartMode___: [^text]

    * Browser startup mode for services with browser logic.
        * Read more about the browser logic in the relevant section in the [FAQ](../FAQ/EN.md#about-browser-logic).

    * The following values are valid:
        * ___"hide"___:
            * The browser will run as a background process and will not interfere with the taskbar.
        * ___"default"___:
            * The browser will start in default mode (as if it were started by the user).
                * When restarting, the browser will also return to default mode, even if the user minimizes the window.
        * ___"minimized"___:
            * Identical to parameter ___"default"___, but, after starting, the browser is minimized.

    * Important:
        * Since the browser logic is automated, user intervention (as in the examples below) can interfere with correct work:
            * Clicking buttons on pages.
            * Opening tabs.
            * Closing the browser window.
            * etc.
        * In the case of such user intervention complaints about incorrect work are not accepted.

1. ### ___seleniumInputSplitMethod___: [^text]

    * Split input text mode, for services with [browser logic](../FAQ/EN.md#about-browser-logic).

    * The following values are valid:

        * ___"all"___:
            * All text will be entered at once.
            * It may freeze if the text is large.
            * Browser automation may be detected.

        * ___"strings"___:
            * The text will be entered line by line.

        * ___"symbols"___:
            * The text will be entered character by character, with no pause between entries.

        * ___"humanTyping"___:
            * Simulated human input with an average typing speed of 450 characters per minute (the real value is randomized).


1. ### ___extraTextOptions___:

    * __"Settings for the displayed text."__ [^inSettingMenu]

    1. ### ___font___: [^text]

        * __"Font."__ [^inSettingMenu]
        * The font with which the text will be displayed.
        * The path to the font file is set relative to the folder ___"%NovelDir%\\game"___, where __%NovelDir%__ is the folder with the game.
            * For example, the font is in a folder:
                * _"C:\\Games\\MyNovel\\game\\fonts\\Comic Sans.otf"_
            * So in the file you have to write:
                * _"fonts/Comic Sans.otf"_
                    * All backslashes (___\\___), if present in the path, should be replaced by forward slashes (___/___).
        * Selecting a font once does not have to be repeated for every game.
            * All used fonts are cached.
                * If you specify in another game a font that was already selected earlier, the file will be added automatically.
                * You can also select a font in the GUI[^GUI] under ___"Pick from the previously used ones"___.

    1. ### ___size___: [^text]

        * __"Size."__ [^inSettingMenu]
        * The size of the displayed text.
        *A positive integer is valid, or an [expression in Ren'Py format](https://www.renpy.org/doc/html/text.html#text-tag-size).

    1. ### ___italic___: [^bool]

        * __"Italic text."__ [^inSettingMenu]
        * When this option is activated, italicizes the displayed text.

    1. ### ___bold___: [^bool]

        * __"Bold text."__ [^inSettingMenu]
        * When this option is activated, it makes the displayed text bold.
