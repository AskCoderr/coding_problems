snail = function (array) {
    // enjoy
    if (array[0].length === 0) {
        return [];
    }
    const li = [];
    let sideLength = array.length - 1;
    const orgSideLength = sideLength;
    let x = 0;
    let y = 0;
    let aState = false;
    let bState = false;
    while (sideLength > 0) {
        for (let i = 0; i < (4 * sideLength); i++) {
            li.push(array[y][x]);
            if (x === orgSideLength - ((orgSideLength - sideLength) / 2) && y === (orgSideLength - sideLength) / 2) {
                aState = !aState;
            }
            else if (x === orgSideLength - ((orgSideLength - sideLength) / 2) && y === orgSideLength - ((orgSideLength - sideLength) / 2)) {
                bState = !bState;
            }
            else if (x === (orgSideLength - sideLength) / 2 && y === orgSideLength - ((orgSideLength - sideLength) / 2)) {
                aState = !aState;
            }
            if (!aState && !bState) {
                x++;
            }
            else if (aState && !bState) {
                y++;
            }
            else if (aState && bState) {
                x--;
            }
            else {
                y--;
            }
        }
        bState = !bState;
        sideLength -= 2;
        x++;
        y++;
    }
    if (array.length % 2 != 0) {
        const temp = (Math.floor(array.length / 2));
        li.push(array[temp][temp]);
    }
    return li;
}

console.log(snail([[1, 2, 3], [8, 9, 4], [7, 6, 5]]));

// https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/javascript
