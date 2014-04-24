$(document).ready(function(){
	$('#partners').jcarousel({
		wrap: 'circular'
	});
	$('#promoslider').jcarousel({
		wrap: 'circular'
	});
	$('#prevslide').click(function() {
		$('#partners').jcarousel('scroll', '-=1');
		return false;
	});
	$('#nextslide').click(function() {
		$('#partners').jcarousel('scroll', '+=1');
		return false;
	});
	
	var slideNav = $('#slidernavlist');
	var slideList = $('#promoslider > ul');
	
	$('.slidernavlink').click(function(e){
		e.preventDefault();
		var slideNum = $(this).parent().index();
		changeslide(slideNum,slideNav,slideList);
		});
	slideNav.find('li:first').find('a').trigger('click');
	var timerId = setInterval(nextSlide, 10000,slideNav);
});

function changeslide(slideNum,slideNav,slideList){
	slideNav.find('a').removeClass('active');
	slideNav.find('li').eq(slideNum).find('a').addClass('active');
	slideList.find('li').eq(slideNum).fadeIn();
	slideList.find('li').not(slideList.find('li').eq(slideNum)).fadeOut(0);
	};
	
function nextSlide(slideNav){
	var nextNum = slideNav.find('.active').parent().index()+1;
	var maxNum = slideNav.find('li').size();
	if(nextNum >= maxNum){
		nextNum = 0;
		}
	slideNav.find('a').eq(nextNum).trigger('click');
	}