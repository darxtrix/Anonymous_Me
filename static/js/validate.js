function validate(evt)
{
	var form = document.getElementById('url_input');
	var supplied_url = form.url.value;
	console.log('supplied_url');
	if ( !supplied_url )
	{
		console.log("No url was supplied");
	} 
	else
	{
		console.log(supplied_url);
	}

}

document.onload = (function()
{
	var form = document.getElementById('url_input');
	form.addEventListener('submit',validate,false);
})();


