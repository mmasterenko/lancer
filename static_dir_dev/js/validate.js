$.validate({
    validateOnBlur : false,
    borderColorOnError : '#ff3300',
    onError : function(){
        $.validate({validateOnBlur : true})
    }
});
