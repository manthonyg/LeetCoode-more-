function bubble_sort(list){
  sorted = false;
  while(!sorted){
    sorted = true;
    for (let i = 0; i < list.length-1; i++){
      if (list[i] > list[i + 1]){
        [list[i],list[i+1]] = [list[i+1],list[i]];
        sorted = false;
      }
    }
  }
  return list;
}

console.log(bubble_sort([2,3,4-1,5,100,2,-99,200]))