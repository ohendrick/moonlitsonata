/**
 * Created by sabir.salman on 1/27/15.
 */
function change() // no ';' here
{
    var elem = document.getElementById("hole");

    if (elem.innerHTML==1) {
        elem.innerHTML = 2;
        elem.value = 2;
    } else {
        elem.innerHTML = 1;
        elem.value = 1;
    }
}

