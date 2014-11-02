function validate(evt)
// Validate the url 
{
	var form = document.url_input; // is there any way of passing form to eventhandler
	evt.preventDefault(); // preventing form from submitting
	var err = document.getElementById('error');
	var urlRegExp =/^(?:(?:https?|ftp):\/\/)(?:\S+(?::\S*)?@)?(?:(?!10(?:\.\d{1,3}){3})(?!127(?:\.\d{1,3}){3})(?!169\.254(?:\.\d{1,3}){2})(?!192\.168(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:\/[^\s]*)?$/i;
	var supplied_url = form.url.value; // getting the user entered url
	if ( !supplied_url )
	{
		err.innerHTML = 'No url supplied';
		err.style.visibility = 'visible';
	} 
	else // if url is supplied then validate the url
	{
		if ( !urlRegExp.test(supplied_url) )
		{
			err.innerHTML = 'Enter a valid url';
			err.style.visibility = 'visible';
		}
		else
		{
			// url is valid , submit the form

			form.submit();
		}

	}
}

window.onload = function()
{
	// css preloader
	var preloader = document.getElementById('loaderWrap');
	preloader.style.display = 'none'; //setting the preloader to turn off
	var content = document.getElementById('content');
	content.style.display = 'block';
	var form = document.url_input; // getting the form
	form.addEventListener('submit',validate,false);
};  


// Responsive font
window.fitText( document.getElementsByTagName('body')[0], 8.0);




