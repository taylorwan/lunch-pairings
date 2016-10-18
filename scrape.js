/* functions for scraping data from sites */
// TODO: automate

// https://fiscalnote.slack.com/team#active
// slack: run on this page
$.each($('.team_list_item .member_name_and_title .member_name'), function() {
	console.log($(this).text())
})

// https://fiscalnote2.atlassian.net/wiki/browsepeople.action
// agora: run on each page
$('.vcard .values h4').text()
