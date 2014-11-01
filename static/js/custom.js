function validate(evt)
// Check whether a url is supplied or not 
{
	var form = document.getElementById('url_input');
	var supplied_url = form.url.value; // getting the user entered url
	if ( !supplied_url )
	{
		console.log("No url was supplied");
	} 
	else
	{
		console.log(supplied_url);
	}
	// make redirect to this particular page if no url is supplied

}

document.onload = function()
{
	var form = document.getElementById('url_input');
	form.addEventListener('submit',validate,false);
};  


// Responsive font
window.fitText( document.getElementsByTagName('body')[0], 7.0);

