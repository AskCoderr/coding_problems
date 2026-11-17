function howManyPiecesOf(myjinxinsHeart) {
  //Happy Coding ^_^
  const arr = [];
  const Xlim = 30;
  const Ylim = 13;
  let ldiag = [];
  let rdiag = [];
  let NoOfFilled = 0

  myjinxinsHeart.split('\n').forEach(element => {
    arr.push(element.split(''))
  });

  for (let y = 0; y <= Ylim; y++) {
    for (let x = 0; x <= Xlim; x++) {
      if (arr[y][x] === 'x') {
        ldiag.push((Ylim - y) + x);
        rdiag.push((Ylim - y) + (Xlim - x))
      }
    }
  }

  ldiag = ldiag.filter((item, index) => {
    return ldiag.indexOf(item) === index;
  })

  rdiag = rdiag.filter((item, index) => {
    return rdiag.indexOf(item) === index;
  })
  ldiag.sort();
  rdiag.sort();
  console.log(ldiag);
  ldiag.forEach(i => {
    if (i <= 14) {
      var x = 1;
      var y = Ylim - (i - 1);
    }
    else if (i > 14) {
      var x = i - 13;
      var y = 0;
    }
    while (x < Xlim && y <= Ylim) {
      if (arr[y][x] != ' ') {
        arr[y][x] = '^';
      }
      x++;
      y++;
    }
  });

  rdiag.forEach(k => {
    if (k <= 14) {
      var x = Xlim - 1;
      var y = Ylim - (k - 1);
    }
    else if (k > 14) {
      var x = Xlim - (k - 13);
      var y = 0;
    }
    while (x > 0 && y <= Ylim) {
      if (arr[y][x] != ' ') {
        arr[y][x] = '^';
      }
      x--;
      y++;
    }

  });

  function filler(a, b) {
    if (arr[a][b] === '*') {
      arr[a][b] = NoOfFilled;
    }
    if (arr[a][b + 1] === '*') {
      filler(a, b + 1);
    }
    if (arr[a][b - 1] === '*') {
      filler(a, b - 1);
    }
    if (arr[a + 1]) {
      if (arr[a + 1][b] === '*') {
        filler(a + 1, b);
      }
    }
    if (arr[a - 1]) {
      if (arr[a - 1][b] === '*') {
        filler(a - 1, b);
      }
    }
  }


  let t = 0
  arr.forEach(row => {
    while (row.includes('*')) {
      let ind = row.indexOf('*')
      filler(t, ind);
      NoOfFilled++;
    }
    t++;
  });

  console.log(arr);
  return NoOfFilled;
}



console.log(howManyPiecesOf(
  `      ******       ******      
    **********   **********    
  ************* *************  
 ********x******************** 
 ***************************** 
 ***************************** 
  *************x*************  
    ***********************    
      *******************      
        ****x**********        
          ***********          
            *******            
              ***              
               *               `));

// answer should be 12

// https://www.codewars.com/kata/599d3a52a8b7539663000052/train/javascript
// i tried so hard and got so far, but in the end it doesnt even matter (aka i got it wrong 😥)
// write filler function again