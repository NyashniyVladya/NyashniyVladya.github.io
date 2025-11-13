// JavaScript Document

async function loadJSON(url) {
    const response = await fetch(url);
    let result;
    if (response.ok) {
        result = await response.json();
        return result;
    };
    result = await response.text();
    throw result;
};

export {loadJSON};
