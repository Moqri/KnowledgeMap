/*
*  @created juni
*  @version $Id: scripts.js , v 1.3 1:47 PM 9/13/2014 juni $
*  -> [REQ_001  - 08.09.2014]
		->  Adding year drop-down filter
		->  Adding source filter
	-> [REQ_002  - 12.09.2014]
		->  Change year drop-down filfer to slider
		->  Remove search filter add move title search to source filter , now "other filter"
		-> 	Add multiple choice source select
 		
*/
$(document).ready(function($){
	$('#source_buttons input:radio').addClass('input_hidden');
	$('#source_buttons label').addClass('selected');//as requested all on at first
	$('#source_buttons label').click(function() {
		//$(this).addClass('selected').siblings().removeClass('selected');
		var elFor = $(this)[0].htmlFor;
		if (elFor!='') {
			if ($(this).hasClass('selected'))  {
				//$("#"+elFor).attr("checked", false); //single option, won't work ;)
				$(this).removeClass('selected')
				$(this).find('img').prop('src', 'images/source_buttons/'+elFor+'_norm.png');
			} else {
				//$("#"+elFor).attr("checked",true);  //single option, won't work ;)
				$(this).addClass('selected');
				$(this).find('img').prop('src', 'images/source_buttons/'+elFor+'_press.png');
			}
		}
	});
	$("#year-slider").rangeSlider({
	  bounds: {min: 2005, max: 2014},
	  defaultValues: {min: 2005, max: 2014},
	});
	//$("#slider-range").rangeSlider({arrows:false});
	// $("#slider-range").rangeSlider("option", "bounds", {min: 2005, max: 2014});
	// Preferred method
 	$("#year-slider").on("valuesChanging", function(e, data){
		var min = Math.round(data.values.min);
		var max = Math.round(data.values.max);
		$("#year_min").val(min);
		$("#year_max").val(max);
		//console.log("Something moved. min: " +min + " max: " + max);
		$GP.year.search(min,max);
	});
	
	$('#source_buttons label').click(function() {//when a source button is pressed
		$GP.year.search($("#year_min").val(),$("#year_max").val());
	});		
});