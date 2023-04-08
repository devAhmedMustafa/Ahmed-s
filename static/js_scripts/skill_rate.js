rateBox = document.querySelectorAll('.rate_box');

rateBox.forEach((element) => {
    let rate = parseInt(element.childNodes[0].value);
    console.log(rate);
    if ( rate < 25 ){
        element.style.backgroundImage = `linear-gradient(to top, hsl(345, ${rate}%, 52%) 0%, #ffb199 100%)`;
    }
    else if ( rate >= 25 && rate < 50 ){
        element.style.backgroundImage = `linear-gradient(120deg, hsl(46, ${rate}%, 68%) 0%, #fda085 100%)`;
    }
    else if ( rate >= 50 && rate < 75 ){
        element.style.backgroundImage = `linear-gradient(to top, hsl(154, ${rate}%, 34%) 0%, #3cba92 100%)`;
    }
    else{
        element.style.backgroundImage = `linear-gradient(to top, hsl(263, ${rate}%, 53%) 0%, #e5b2ca 100%)`;
    }
    element.style.width = `${rate}%`;
});


