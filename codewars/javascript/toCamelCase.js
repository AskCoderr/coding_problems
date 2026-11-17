function toCamelCase(str) {
    if (str === '') {
        return '';
    }
    var arr = str.split('');
    var state = false;
    var newStr = '';
    newStr += arr.shift();
    arr.forEach(element => {
        if (['-', '_'].includes(element)) {
            state = true;
        }
        else if (state) {
            newStr += element.toUpperCase();
            state = false;
        }
        else {
            newStr += element.toLowerCase();
        }
    });
    return newStr;
}
console.log(toCamelCase('hello_world'));
// https://www.codewars.com/kata/517abf86da9663f1d2000003/train/javascript