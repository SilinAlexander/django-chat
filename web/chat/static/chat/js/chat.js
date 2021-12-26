$(function () {
  $('.chat-list').click(makeActiveChat)
});

function makeActiveChat(){
let chat_id = $(this).attr('id')
if($(this).attr('id') === $('.chat-history').attr('chat-id')) return
console.log('click', $(this).attr('id'), $('.chat-history').attr('chat-id'))
$('.chat-history').attr('chat-id', $(this).attr('id'))

}
