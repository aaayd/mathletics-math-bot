// !!! THIS IS UNFINISHED 
// Automatically inputting requires getting an AngularJS element via an external JS file, and I am not wasing any more time on this

// This will just send input to a box. It will not automatically submit like the py script

question = document.getElementsByClassName("question-size-v4")[0].innerText.slice(0, -3);
input_box = document.getElementsByClassName("questions-input-adjustment")[0]
answer = eval(`${question}`);

console.log(`Question: {question} = ${answer}`);
input_box.value = answer;
