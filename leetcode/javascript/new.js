/**
 * @param {number} num
 * @return {string}
 */

const primary = { 0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen" };
const secondary = { 0: "", 2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety" };
const tertiary = ["Thousand", "Million", "Billion"];

var numberToWords = function (num) {
    if (num === 0) {
        return "Zero";
    }
    const groups = [];
    let result = [];
    num = num.toString();
    if (num.length >= 3) {
        for (let i = 1; i <= num.length - (num.length % 3); i += 3) {
            groups.push(num.slice(num.length - i - 2, num.length - i + 1));
        }
    }
    if (num.length % 3 !== 0) {
        groups.push(num.slice(0, num.length % 3));
    }
    groups.reverse();

    for (let k = 0; k <= groups.length - 1; k++) {
        let current = groups[k];
        while (current.startsWith("0")) {
            current = current.slice(1,);
        }
        const length = current.length;
        let temp = [];

        switch (length) {
            case 3:
                temp.push(primary[parseInt(current[0])]);
                temp.push("Hundred");
                if (current[1] === "1") {
                    temp.push(primary[parseInt(current.slice(1, 3))]);
                } else {
                    temp.push(secondary[parseInt(current[1])]);
                    temp.push(primary[parseInt(current[2])]);
                }
                break;

            case 2:
                if (current[0] === "1") {
                    temp.push(primary[parseInt(current)]);
                } else {
                    temp.push(secondary[parseInt(current[0])]);
                    temp.push(primary[parseInt(current[1])]);
                }
                break;

            case 1:
                temp.push(primary[parseInt(current)]);
                break;
        }

        if (k < groups.length - 1 && temp.length !== 0) {
            temp.push(tertiary[groups.length - k - 2]);
        }
        temp.forEach((item) => {
            result.push(item);
        })
    }

    result = result.filter(item => item !== "");
    return result.join(" ");
};

console.log(numberToWords(1000000));


// https://leetcode.com/problems/integer-to-english-words/description/