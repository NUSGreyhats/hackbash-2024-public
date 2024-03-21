const generate = (length) => {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}

const queryString = window.location.search;
const parameters = new URLSearchParams(queryString);
const username = parameters.get('username');
const usernameLength = parameters.get('length');

if (username) {
    document.getElementById('generatedUsername').innerHTML = `Your generated username is: ${username}`;
} else if (usernameLength) {
    window.location.href = `/?username=${generate(usernameLength)}`;
}