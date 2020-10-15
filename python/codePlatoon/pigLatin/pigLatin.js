function translate(word){
  let allWords = word.split(' ');
  let newAllWords 
  newAllWords = allWords.map(x=>transform(x));
  return newAllWords.join(' ')
}

function transform(word){
  const vowelArr = ['a', 'e', 'i', 'o', 'u'];
  const punctuations = [',','.','?'];
  let letters = word.split('');

  if (vowelArr.includes(letters[0])){
    letters.push('ay');
    return letters.join('');
  }
  else{
    
    if (letters[0] == 'q' && letters[1] == 'u'){
      letters.splice(0,2,'qu')
    }
    let count = 0;
    let maxCount = letters.length;
    
    //extract punction if there is one
    let lastLetter = letters[letters.length-1];
    let punction = '';
    if (punctuations.includes(lastLetter)){
      punction = letters.pop();
    }

    //deal with if first letter is uppercase
    let firstLetter = letters[0];
    let firstLetterIsUpperCase = false;
    if (firstLetter == firstLetter.toUpperCase()){
      firstLetterIsUpperCase = true;
    }

    while (!vowelArr.includes(letters[0]) && count < maxCount){

      letters.push(letters.shift());
      count ++;
    }
    if (firstLetterIsUpperCase){
      letters = letters.map(x=>x.toLowerCase());
      letters[0] = letters[0].toUpperCase()
    }
    letters.push('ay');
    if (punction){
      letters.push(punction); // add punctuation
    }
    return letters.join('');
  }
  
}


console.log(translate('apple university'))
console.log(translate('apple school'))
console.log(translate("I go to apple university"))
console.log(translate("Hi, I'm Zach"))
console.log(translate("the quick brown fox"))

exports.translate = translate;