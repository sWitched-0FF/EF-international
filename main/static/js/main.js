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

	$('.accordiontitle').click(function(){
		$(this).siblings().slideToggle();
		$(this).parent().toggleClass('closed');
		});
	$('.tabscontrol a').click(function(e){
		e.stopPropagation();
		var indextab = $(this).parent().index();
		$(this).parent().siblings().removeClass('active');
		$(this).parent().addClass('active');
		$(this).parent().parent().parent().find('.tabsblockpage:eq('+indextab+')').addClass('active').siblings().removeClass('active');
		});
	$('.tabsblockpage').fancyfields();
	$('.newssubscribefilter').fancyfields();
	$('.eventsfilter select,.eventsfilter input[type!=text]').fancyfields();
	$('.scroll-pane').jScrollPane({
		showArrows: true,
		autoReinitialise: true
		});
	$('#subscribe').click(function(){
		$('#overlay').fadeIn();
		return false;
		});
	$('#overlay, #closemodal').click(function(){
		$('#overlay').fadeOut();
		});
	$('.modalbox').click(function(){
		return false;
		});
	$('.dateui').datepicker();
	
	partnerlistsort($('#partners'),$(document).width());
});
$(window).resize(function(){
	partnerlistsort($('#partners'),$(document).width());
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

function partnerlistsort(obPartners,screenWidth){
	if(screenWidth < 1830){
		var partnerList = '<ul class="partnerslist">';
		$.each($('.partnerbox'),function(i,val){
			if(i%2){
				partnerList+='<a href="'+$('.partnerbox:eq('+i+')').attr('href')+'" class="partnerbox">'+$('.partnerbox:eq('+i+')').html()+'</a></li>';
				}
			else{
				partnerList+='<li class="partnerscell"><a href="'+$('.partnerbox:eq('+i+')').attr('href')+'" class="partnerbox">'+$('.partnerbox:eq('+i+')').html()+'</a>';
				}
			});
		partnerList+='</ul>'
		obPartners.html(partnerList);
		obPartners.jcarousel('reload',{
			wrap: 'circular'
		});
		}
	else{
		var partnerList = '<ul class="partnerslist">';
		$.each($('.partnerbox'),function(i,val){
			if((i%5)==4){
				partnerList+='<a href="'+$('.partnerbox:eq('+i+')').attr('href')+'" class="partnerbox">'+$('.partnerbox:eq('+i+')').html()+'</a></li>';
				}
			else if((i%5)==0){
				partnerList+='<li class="partnerscell"><a href="'+$('.partnerbox:eq('+i+')').attr('href')+'" class="partnerbox">'+$('.partnerbox:eq('+i+')').html()+'</a>';
				}
			else{
				partnerList+='<a href="'+$('.partnerbox:eq('+i+')').attr('href')+'" class="partnerbox">'+$('.partnerbox:eq('+i+')').html()+'</a>';
				}
			});
		partnerList+='</ul>'
		obPartners.html(partnerList);
		obPartners.jcarousel('reload',{
			wrap: 'circular'
		});
		}
	}