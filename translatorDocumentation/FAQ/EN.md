
# Answers to questions and general information..

___

## General Information.

1. ### What kind of project is this?

    * **Translator3000** is an automatic translator for games made on the Ren'Py engine, with an easy installation and user-friendly interface.

    * Want to read a visual novel and it doesn't have a translation in your language?
        * All you need to do is copy the file **Translator3000.rpa** into the folder with the game.
            * Read more about installation [here](./EN.md#where-to-begin).

    * More information about the functions and features of the translator is provided in the following sections of the documentation.

1. ### Links.

    1. #### [Discord Community.](https://discord.gg/FqsQXNH6Fg)

        * Here you can find a link to the latest version, chat with other translator users, and search for an answer to your question in the Question Channel.

    1. #### [Boosty.](https://boosty.to/nyashniyvladya)

        * Here you can support the project and download the latest version of the translator.

1. ### About Versions.

    * There are two versions of the translator:

        1. #### Trial version.

            * You can download it [here](https://github.com/NyashniyVladya/Translator3000).
            * Available for download to all without exception.
            * Trial version with limited functionality, to get acquainted with the translator.

        1. #### Main version.

            * You can subscribe and download on [Boosty](https://boosty.to/nyashniyvladya?postsTagsIds=124156).

            * The version is distributed according to the [subscription model](https://en.wikipedia.org/wiki/Subscription_business_model).

            * Version with full functionality, updates and bug fixes.

            * #### ___Important___:

                * Only the latest version is supported.
                * Bug reports are only accepted for the latest version.
                    * As the translator is constantly being worked on, an error that occurred in earlier versions may no longer be present in later versions.
                    * [More about the format of bug reports](./EN.md#about-bugs-and-errors).


1. ### Where to begin?

    * So. You signed up for [Boosty](https://boosty.to/nyashniyvladya), downloaded ___Translator3000.rpa___ and don't know what to do with it. Let me explain.

    1. Copy the file to the folder __game__ in the directory of the game for which you need a translation.
    1. Launch the game.
    1. In the upper left corner you will see the GUI window of the translator.
        * Here you can set up the parameters you need.
        * The settings can also be made via a [configuration file](./EN.md#noveldir_translator3000_settingjson).
        * See the [parameter description page](../settingDescription/EN.md#parameter-description) for details.
    1. [Enjoy the game.](./EN.md#the-best-optimal-for-comfortable-reading-use-is-as-follows)


1. ### About translator work modes.

    * Translator can work in three switchable modes:

        1. #### Real-time translation.

            * The translation takes place at the moment when the game passes the string to the display.
            * If there is a string in the translations database, the cached translation is displayed immediately.
            * if the string isn't in the translation database (the string has never been displayed and there was no prescan), there will be a request to the translation service.
                * This will inevitably cause a "freeze", because a network request will be executed.

        1. #### Translation only from the database.

            * Similar to the previous mode, but with one important change:
                * If a string isn't in the translation database, it will not be translated, but the original text will be displayed.

            * This mode is very useful in novels-sandboxes, where there is a lot of permanently updated data.
                * When this mode is activated, with the performed prescan, the permanent text (dialogues, etc.) will be translated, while the dynamic data (date, game time, etc.) will be output as it is.

        1. #### Prescan.

            * Pre-translate all strings in the game and compile a database of translations, to neutralize "freezes" at the moment of switching strings.
            * When activated, the translator collects all the strings in the game, groups it and translates them sequentially.
            * If the game has dynamic data (player name, etc.), it is better to enter it __before__ running the prescan.
                * This is needed to correctly translate strings where dynamic data substitution is used.
            * If a novel is large, the process can take a long time.

    * #### The best (optimal for comfortable reading) use is as follows:

        1. Run the novel.
        1. Get to the place where the game asks you to enter the player name / other dynamic data (if any).
            * If there is no dynamic data input, just run the game anywhere.
        1. Enter data (if required).
        1. Start the translator in prescan mode with the corresponding item in the GUI.
        1. Wait for the prescan to complete.
            * Depending on the size of the novel, prescanning can take a long time.
            * If the novel is extremely large, it makes sense to leave it in the translation process and do something else in the meantime until the translation is complete.
        1. Switch to the translation mode ___"only from the database"___.
        1. Hide the translator's GUI and enjoy the novel.


1. ### About Database.

    * Any text translated either by prescanning or in real time is stored in a database on the user's device.

    * #### Global Database.

        * The first time you start the translator, it creates a global database that stores the translations of all the novels that have ever been translated.

    * #### Local Database.

        * In addition to the global database, each novel creates its own (local) database.

    * #### Database Import.

        * If anyone has already completed the novel, he can share his database (local, or global).
        * To use a translation from another person, just copy their database to the [___imported translations___](./EN.md#noveldirlocal-translationsservicenameimported-translations) folder.
        * After launching, the game imports the translation into the local game database and the global database.
        * After a successful import, the imported file will be deleted.
        * ___Important:___
            * As indicated earlier, the translation is made with the insertion of dynamic data, so that if the creator of the database has entered different data, the strings containing this data will need to be re-translated, taking into account the new values.
        * Collected databases can be found in the [Discord community](https://discord.gg/FqsQXNH6Fg).

    * #### About database formats.

        * Although database formats have changed as the translator has evolved, importing databases in the old format works.

    * #### About backups.
        * If your database is broken for some reason, the translator always creates, next to the database files, a backup copy of the previous version with the ___.oldBackup___ extension.
        * To restore the database, delete the original database file and rename the backup file, removing the ending ___.oldBackup___ from it.
            * Your system may have turned off the display of file name extensions. In this case, enable this feature in the way that your operating system does.


1. ### About "browser logic".

    * Some translation services use real browser actions to work.
    * #### The [selenium](https://www.selenium.dev)/[chromedriver](https://chromedriver.chromium.org/home) stack is used for automation.
    * #### The [Google Chrome browser](https://www.google.com/chrome) must be installed in the OS to work correctly.

        * Versions newer than 70 are supported.
            * It is, of course, better to use the latest version.

    * #### Since this logic completely mimics the user's actions (opening a page, pressing buttons, entering text), translation can take an extremely long time. It is recommended to use __only__ with prescanning.

    * #### By default, the graphical part of the browser is disabled.

        * You can enable it if you want. Read more in the [documentation of the setup file](../settingDescription/EN.md#seleniumstartmode-).


1. ### Where is what and what files the translator uses and creates.

    * The following conventions will be used:

        * ___%UserName%___:
            * Current username.

        * ___%userprofile%___:
            * The path to the user's home folder. May be different on different systems.
                * Default is in Windows:
                    * ___С:\\Users\\%UserName%___
                * Default in UNIX-like:
                    * ___/home/%UserName%___
                * Default in Mac:
                    * ___/Users/%UserName%___

        * ___%ServiceName%___:
            * The name of one of the translation services.

        * ___%NovelDir%___:
            * Game directory.
                * The one with the ___game___, ___renpy___ folders and the executable launch file

    * Paths will be written in Windows format (with backslashes), change to forward slashes if necessary.

    * This is a complete list of working paths. Depending on how the translator is used, some of them may not exist.

    1. #### __*%userprofile%\\vladya's projects database*__:

        * The main folder for storing data from the different modules.

    1. #### __*%userprofile%\\vladya's projects database\\selenium*__:

        * The main folder of the __selenium__ module, which is responsible for the browser logic.

    1. #### __*%userprofile%\\vladya's projects database\\selenium\\chromedriver*__:

        * The folder with the executable files of the ___chromedriver___ module, which is responsible for automating actions in the browser.
        * Contains folders with the version numbers of the browser, which contain folders with the version numbers of the ___chromedriver___ module, which contain the executable file of the ___chromedriver___ module.

    1. #### __*%userprofile%\\vladya's projects database\\translator3000*__:

        * Translator's main folder.

    1. #### __*%userprofile%\\vladya's projects database\\translator3000\\%ServiceName%*__:

        * The folder with the global (for all novels) database of translations of one of the services.
        * Contains folders with database version numbers, which contain database file ___translations___ (the format can be different).

    1. #### __*%userprofile%\\vladya's projects database\\translator3000\\Ren'Py MuitiGame Data.pickle*__:

        * A file that stores data that can be transferred between games, such as previously used fonts, translation service settings, etc.

    1. #### __*%NovelDir%\\_translator3000_setting.json*__:

        * File with the translator settings for a particular game.
        * [File content information.](../settingDescription/EN.md#description-of-the-parameters-and-settings-file)

    1. #### __*%NovelDir%\\local translations\\%ServiceName%*__:

        * A folder with a local (for a particular novel) database of translations for one of the services.
        * Contains folders with database version numbers, which contain database file ___translations___ (the format can be different).
        * It also contains the [___imported translations___](./EN.md#noveldirlocal-translationsservicenameimported-translations) folder for importing completed translations.

    1. #### __*%NovelDir%\\local translations\\%ServiceName%\\imported translations*__:

        * A folder for importing completed translations.
        * The instructions for importing translations are described [above](./EN.md#database-import).

    1. #### __*%NovelDir%\\_translator3000Data*__:

        * A folder for working files, for a particular novel.

    1. #### __*%NovelDir%\\_translator3000Data\\debug*__:

        * Files for debugging the translator.

    1. #### __*%NovelDir%\\_translator3000Data\\debug\\lastLog.log*__:

        * Log file containing technical information about the translator's actions.
        * If parameter [___\_debug_mode___](../settingDescription/EN.md#_debug_mode-) is activated, full information will be written to the file, otherwise only basic data and error information will be written.

    1. #### __*%NovelDir%\\_translator3000Data\\temp*__:

        * Temporary translator files.

    1. #### __*%NovelDir%\\_translator3000Data\\temp\\cacert.pem*__:

        * The certificate file for the ___requests___ module.
        * Generated only in older versions of Ren'Py.
            * In Ren'Py versions newer than 7.4.0, the ___requests___ module is [part of the engine](https://www.renpy.org/doc/html/changelog.html#renpy-7-4).

    1. #### __*%NovelDir%\\game\\Translator3000.rpa*__:

        * The translator itself.

    1. #### __*%NovelDir%\\game\\translator3000_ingame_files*__:

        * A folder with the translator files used in the novel.

    1. #### __*%NovelDir%\\game\\translator3000_ingame_files\\multigame_fonts*__:

        * The folder where fonts from other novels will be copied when they are selected.

    1. #### __*%NovelDir%\\game\\translator3000_ingame_files\\pc_fonts*__:

        * The folder where fonts will be copied to when they are selected in the GUI from computer files.


1. ### About bugs and errors.

    * Bug reports are only accepted for the latest actual version.
        * [Read more here.](./EN.md#important)

    * #### What to do when errors occur:

        1. Make sure you have the [latest version of the translator](./EN.md#important).

        1. Replay the situation in another novel and make sure the error repeats itself.
            * If the error occurs in a single novel, read the [corresponding paragraph of the FAQ](./EN.md#the-game-insert-game-name-does-not-translatedoes-not-startdoes-not-work-correctly).

        1. If an error occurs during a prescan, click "Raise traceback" in the GUI to generate an error report.

        1. ##### Prepare the following data needed by the developer for debugging:

            1. Log file:
                * How to correctly generate a log file:
                    1. Activate [debug mode](../settingDescription/EN.md#_debug_mode-).
                    1. Go to the point where the error occurs.
                * Where is the log file?
                    * Read the [previous section of the documentation, describing the paths](./EN.md#noveldir_translator3000datadebuglastloglog).

            1. Information about the settings.
                * Translator's work mode, service, etc.

            1. The file ___traceback.txt___, which is in the game directory.
                * If it exists.

            1. Information about what actions caused the error.

            1. If the error occurs with the translation service with [browser logic](./EN.md#about-browser-logic), set the ___"default"___ value for the [___"seleniumStartMode"___](../settingDescription/EN.md#seleniumstartmode-) setting and add information in the error message about whether it affected the operation.

            1. Any other information you deem relevant in the context of this question.

        1. Read [this section of the documentation](./EN.md#i-did-not-find-an-answer-to-my-question-in-this-documentation) and, if your question has not yet been answered, ask it in the question channel.


    * Description of some errors:

        * The error type will be written in the traceback, before the description of the error, or at the end, after the translation text.

        1. ##### ___ShadowBan___:

            * The "shadow" ban error. May occur with services that have recognized automation.
            * Occurs in the case of a long and consistent translation of extremely large novels.

___


## Q&A.


1. ### ___I have "squares" instead of text.___

    * Change the font to one that supports the language you want.
        * [Instructions for installing the font.](../settingDescription/EN.md#font-)

        * ### ___Where can I find fonts?___

            * Search for "download fonts" in any search engine.
        * TrueType/OpenType fonts are supported.


1. ### ___The game \<insert game name\> does not translate/does not start/does not work correctly.___

    * How a game is made depends on the developer. Depending on the implementation, there may be conflicts in particular games. Get over it. There is nothing I can do here. Compatibility with all games in the universe, unfortunately, can not be realized.


1. ### ___How do I launch the GUI of the translator?___

    * ***Alt***+***~*** (tilde) key combination (simultaneous pressing).

        1. #### Why did you make such a strange choice?

            * Because of the compatibility question. I'm trying to make my translator as versatile as possible, and this combination is unlikely to be used anywhere else.

            1. #### Can I change it?

                * Some day, some time... At this point, as far as I know, there has never been a conflict of combinations in games, which means the choice is correct.


1. ### The translator removes tags from the original game (italics, bold text, color, etc.).

    * Yep. It does that. It also removes tags like ***{w}***/***{nw}*** and the like.
    * This is done because tags cannot be escaped when requesting a translation service.
        * To ***"{color=...}"*** the service may return ***"{цвет=...}"***, which of course will cause an error.
        * It is possible, of course, to translate in parts (a passage before the tag, a passage after it, etc.), but in this case the quality of the translation will suffer greatly, because the words will be translated without taking into account all the context and will not be connected to each other.
        * I see no way to "painlessly" keep the tags, so I decided to remove them altogether.


1. ### How do I run the translator on Android?

    * No idea. I write the translator for the PC version. I have never programmed for phones and do not know how to do it.
    * As far as I heard, there seem to be some ports from third-party developers, but they have nothing to do with me or the project. Use them only at your own risk.


1. ### ___I did not find an answer to my question in this documentation.___

    * Look at the question channel in the [translator's Discord community](https://discord.gg/FqsQXNH6Fg). Most likely a similar question has already been answered there.

    * If there is no answer, ask your question there.
        * ___Exactly in the question channel.___
            * ___Not in private messages to the translator's author.___
            * ___Not in private messages to the moderator.___

        * By asking your question in private messages, you deprive others of the opportunity to see the answer if they have similar problems and, among other things, you force the administrator/moderator to repeat the same things several times.
            * Which is no fun at all.
            * Not at all.
            * Not. At. All.

        * If you report an error, be sure to [attach the data necessary to resolve the error](./EN.md#prepare-the-following-data-needed-by-the-developer-for-debugging).


1. ### ___I still don't understand something in this documentation. Can I write to you in a private message, on a social network, by e-mail, or anywhere else?___

    * No.


1. ### ___But I...___

    * No.


1. ### ___But...___

    * No.
