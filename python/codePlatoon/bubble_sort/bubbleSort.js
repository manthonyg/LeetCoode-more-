function bubble_sort(list){
  let sorted = false;
  let endIndex = list.length - 1
  while(!sorted){
    sorted = true;
    for (let i = 0; i <= endIndex; i++){
      // console.log(list[i])
      if (list[i] > list[i + 1]){
        [list[i],list[i+1]] = [list[i+1],list[i]];
        sorted = false;
      }
    }
    endIndex--;
  }
  return list;
}

console.log(bubble_sort([2,3,4-1,5,100,2,-99,200,1]))