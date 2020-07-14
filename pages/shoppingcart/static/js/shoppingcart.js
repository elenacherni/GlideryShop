function checkStatusRemove(){
    const submitRemove = document.getElementById("submitRemove");
    const countCheckSelectedRemove = document.querySelectorAll('input[type=checkbox]:checked').length;

    if (countCheckSelectedRemove == 0){
        alert("לא נבחרו פריטים למחיקה");
    } else if (countCheckSelectedRemove == 1){
        submitRemove.click();
        alert("הפריט נמחק בהצלחה");
    } else {
        submitRemove.click();
        alert("הפריטים נמחקו בהצלחה");
    }
}//checkStatusCookie