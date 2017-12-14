$(document).ready(function() {
    $('.edit-profile-ico').click(function() {
        $('.saved-profile').hide();
        $('.editable-profile').show();
    });
    $('.cancel-profile-changes').click(function(){
        $('.saved-profile').toggle();
        $('.editable-profile').toggle();
    })
})