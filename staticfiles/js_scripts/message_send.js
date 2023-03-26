leavemsg = document.querySelector('#msg');
msgfield = document.querySelector('#msgfield');
textField = document.querySelector('#text_field')

leavemsg.addEventListener('click', function () {
    msgfield.style.display = 'flex';
})

sendBtn = document.querySelector('#send_msg');

sendBtn.addEventListener('click', function () {
    if ( textField.value.trim() == "" ){
        textField.style.border = '1px solid red';
    }
    else{
        textField.style.border = '1px solid black';
        $.ajax({
            url: '/send_msg/',
            data: {'message': textField.value},
            success: function(data){
                sendBtn.style.backgroundColor = 'green';
                sendBtn.innerHTML = 'Sent';
                textField.value = '';
                console.log(data.message);
                setTimeout(function(){
                    sendBtn.innerHTML = 'Send';
                    sendBtn.style.backgroundColor = 'white';
                    sendBtn.style.color = 'black';
                }, 2000)
            }
        })
    }

    
    
})