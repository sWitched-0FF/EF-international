$(document).ready(function(){
	$('#partners').jcarousel({
		wrap: 'circular'
	});
	$('#promoslider').jcarousel({
		wrap: 'circular'
	});
	$('#banners').jcarousel({
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
	$('#prevbanner').click(function() {
		$('#banners').jcarousel('scroll', '-=1');
		return false;
	});
	$('#nextbanner').click(function() {
		$('#banners').jcarousel('scroll', '+=1');
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
	$('.tabscontrol > li > a').click(function(e){
		e.stopPropagation();
		var indextab = $(this).parent().index();
		$(this).parent().siblings().removeClass('active');
		$(this).parent().addClass('active');
		$(this).parent().parent().parent().find('.tabsblockpage:eq('+indextab+')').addClass('active').siblings().removeClass('active');
		});

	$('.eventsfilter select,.eventsfilter input[type!=text],input[type=checkbox]:not(.newsfilter input[type=checkbox])').fancyfields();
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
	
	$('.newsfilter input[type=checkbox]').fancyfields({
		onCheckboxChange: function (input, isChecked) {
			input.closest('form').submit();
		}
	});
	
	partnerlistsort($('#partners'),$(document).width());
	bannersResort($('#banners'),$(document).width());
	
	//animate languages list on hover
	$('.languageselect ul').hover(
		function(){
			$(this).animate({height:($(this).find('li').length-1)*27+'px'},400);
			},
		function(){
			$(this).animate({height:"0px"},400);
			});
	//submit language form on click
	$('#languageselect .languageicon').click(function(e){
		e.stopPropagation();
		$('#languageselect input[name=language]').val($(this).attr('href').substring(1));
		$('#languageselect').submit();
		});
});
$(window).resize(function(){
	partnerlistsort($('#partners'),$(document).width());
	bannersResort($('#banners'),$(document).width());
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

function bannersResort(obBanners,screenWidth){
	if(screenWidth < 1830){
		var bannersList = '<ul class="bannerslist">';
		$.each($('.infobanner'),function(i,val){
			bannersList+='<li>'+$('.infobanner:eq('+i+')').parent().html()+'</li>';
			});
		bannersList+='</ul>';
		obBanners.html(bannersList);
		obBanners.jcarousel('reload',{
			wrap: 'circular'
		});
		$('#noslidebanner').hide().html('');
	}
	else{
		var bannersList = '<ul class="bannerslist">';
		$.each($('.infobanner'),function(i,val){
			if(i){
				bannersList+='<li>'+$('.infobanner:eq('+i+')').parent().html()+'</li>';
			}
			});
		bannersList+='</ul>';
		$('#noslidebanner').html($('.infobanner:eq(0)').parent().html()).fadeIn();

		obBanners.html(bannersList);
		obBanners.jcarousel('reload',{
			wrap: 'circular'
		});
		}
	}