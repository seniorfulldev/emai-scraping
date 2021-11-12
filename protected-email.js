function cfDecodeEmail(encodedString) {
    var email = "", r = parseInt(encodedString.substr(0, 2), 16), n, i;
    for (n = 2; encodedString.length - n; n += 2){
        i = parseInt(encodedString.substr(n, 2), 16) ^ r;
        email += String.fromCharCode(i);
    }
    return email;
}

console.log(cfDecodeEmail("8bf8fefbfbe4f9ffcbecfee5e8f9e2ffe2e8a5e8e4e6")); // usage