function main()
{
/*  var $skillset = $('.skillset');
  alert($skillset) 	*/
  $('.toggle').hide();
  $('.built-room').hide();
  $('.room').on('click', function(){
    $(this).toggleClass('active');
    $(this).next().slideToggle(400);
  });
}
$(document).ready(main);