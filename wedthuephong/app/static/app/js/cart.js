
var updateBtns = document.getElementsByClassName('update-cart')
for(i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click', function(){
        var idphong = this.dataset.idphong
        var action = this.dataset.action
        console.log('idphong:',idphong,'action:',action)
        console.log('user: ',user)
        if (user === "AnonymousUser"){
            console.log('data')
        }else{
            updateUserorder(idphong,action)  
        }
    })
}
function updateUserorder (idphong,action){
    console.log('user đã đăng nhập')
    var url= '/update_item/'
    fetch(url,{
        method:'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'idphong':idphong,'action':action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data',data)
        location.reload()
    })
}