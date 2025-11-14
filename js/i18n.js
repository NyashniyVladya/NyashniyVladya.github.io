
import * as utils from "./utils.js";

class Localizer {

    TAG_NAME = "data-i18n";
    AVAILABLE_LOCALES = {
		"en": "English",
		"ru": "Russian"
	};

    constructor() {
        this.locale = this.detectLocale();
    };

    detectLocale() {

        console.debug("Try to detect locale");
        let variants = [localStorage.getItem("locale"), ];

        if (navigator.languages) {
            navigator.languages.forEach(
                ((lng) => variants.push(lng))
            );
        };
        variants.push(navigator.language);
        variants.push(navigator.userLanguage);
        variants.push("en", "ru");

        for (let variant of variants) {
            console.debug(`Check variant: \"${variant}\"`);
            if (variant) {
                variant = variant.trim().toLocaleLowerCase();
                for (let lng in this.AVAILABLE_LOCALES) {
                    if (variant.startsWith(lng)) {
                        return this.AVAILABLE_LOCALES[lng];
                    };
                };
            };
        };

        console.error(`No variant was found`);
        return null;
    };

    updatePage(new_locale=null) {

        if (new_locale !== null) {
            this.locale = new_locale;
        };

        const selector = document.getElementById("languageSelect");
        for (let i = 0; (i < selector.length); i++) {
            const op = selector.options[i];
            if (this.locale == op.value) {
                selector.selectedIndex = i;
                break;
            };
        };

        const translatesPromise = utils.loadJSON(`locales/${this.locale}.json`);
        translatesPromise.then(translates => {
            const elements = document.querySelectorAll(`[${this.TAG_NAME}]`);
            for (let element of elements) {
                const key = element.getAttribute(this.TAG_NAME);
                const value = translates[key];
                if (value === undefined) {
                    continue;
                };
                element.innerHTML = value;
            };
        });

    };
};


window.localizer = new Localizer();
window.onload = function() {
    const selector = document.getElementById("languageSelect");
    selector.onchange = function(ev) {
        console.info(`Press button on selector: ${ev.target.value}`)
        localStorage.setItem("locale", ev.target.value);
        window.localizer.updatePage(ev.target.value);
    };
    window.localizer.updatePage();
};
