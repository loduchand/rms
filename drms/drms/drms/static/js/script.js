$('#mybtn').on('click', function(event) {
	console.log("piyush");
    event.preventDefault(); 
    var url = $(this).data('target');
    location.replace(url);
});

function open_win(job) {
	console.log(job)
	window.open("http://127.0.0.1:8000/job=" + job)
	}