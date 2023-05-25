$(document).ready(function() {
	// Обработчик для кнопки "Далее"
  $(document).on('click', '.servicePage', function() {
    const hasActiveTime = $('.time__items .time__elems_elem .time__elems_btn.active').length > 0;
    const hasSelectedService = $('.service__form_block > button.selected').length > 0;

    if (hasActiveTime && hasSelectedService) {
      $('.time__btns_next').addClass('active');
    } else {
      $('.time__btns_next').removeClass('active');
    }
  });
 // Обработчик клика на кнопках времени
  $(document).on('click', '.time__elems_btn', function(e) {
    e.preventDefault();
    $('.time__elems_btn').removeClass('active');
    $(this).addClass('active');
  });

	$('.salonsSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  infinite: true,
	  prevArrow: $('.salons .leftArrow'),
	  nextArrow: $('.salons .rightArrow'),
	  responsive: [
	    {
	      breakpoint: 991,
	      settings: {

	      	centerMode: true,
  			//centerPadding: '60px',
	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});
	$('.servicesSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  prevArrow: $('.services .leftArrow'),
	  nextArrow: $('.services .rightArrow'),
	  responsive: [
	  	{
	      breakpoint: 1199,
	      settings: {


	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 991,
	      settings: {

	      	centerMode: true,
  			//centerPadding: '60px',
	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});

	$('.mastersSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  prevArrow: $('.masters .leftArrow'),
	  nextArrow: $('.masters .rightArrow'),
	  responsive: [
	  	{
	      breakpoint: 1199,
	      settings: {


	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 991,
	      settings: {


	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});

	$('.reviewsSlider').slick({
		arrows: true,
	  slidesToShow: 4,
	  prevArrow: $('.reviews .leftArrow'),
	  nextArrow: $('.reviews .rightArrow'),
	  responsive: [
	  	{
	      breakpoint: 1199,
	      settings: {


	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 991,
	      settings: {


	        slidesToShow: 2
	      }
	    },
	    {
	      breakpoint: 575,
	      settings: {
	        slidesToShow: 1
	      }
	    }
	  ]
	});

	// menu
	$('.header__mobMenu').click(function() {
		$('#mobMenu').show()
	})
	$('.mobMenuClose').click(function() {
		$('#mobMenu').hide()
	})

	new AirDatepicker('#datepickerHere')

	var acc = document.getElementsByClassName("accordion");
	var i;

	for (i = 0; i < acc.length; i++) {
	  acc[i].addEventListener("click", function(e) {
	  	e.preventDefault()
	    this.classList.toggle("active");
	    var panel = $(this).next()
	    panel.hasClass('active') ?
	    	 panel.removeClass('active')
	    	:
	    	 panel.addClass('active')
	  });
	}


	$(document).on('click', '.accordion__block', function(e) {
		let thisName,thisAddress;

		thisName = $(this).find('> .accordion__block_intro').text()
		thisAddress = $(this).find('> .accordion__block_address').text()

		$.ajax({
            data: {'address': thisAddress},
            url: "/get_masters/",
            // on success
            success: function (response) {
                if (response) {
                    $('.service__masters > .panel').html(response)
                }
            },
            // on error
            error: function (response) {
            console.log('Error')
            }
        });


		$(this).parent().parent().find('> button.active').addClass('selected').text(thisName + '  ' +thisAddress)
		setTimeout(() => {
			$(this).parent().parent().find('> button.active').click()
		}, 200)

		// $(this).parent().addClass('hide')

		// console.log($(this).parent().parent().find('.panel').hasClass('selected'))

		// $(this).parent().parent().find('.panel').addClass('selected')
	})


	$('.accordion__block_item').click(function(e) {
		let thisName,thisAddress;
		thisName = $(this).find('> .accordion__block_item_intro').text()
		thisAddress = $(this).find('> .accordion__block_item_address').text()
		$(this).parent().parent().parent().parent().find('> button.active').addClass('selected').text(thisName + '  ' +thisAddress)
		// $(this).parent().parent().parent().parent().find('> button.active').click()
		// $(this).parent().parent().parent().addClass('hide')
		setTimeout(() => {
			$(this).parent().parent().parent().parent().find('> button.active').click()
		}, 200)
	})



	// 	console.log($('.service__masters > .panel').attr('data-masters'))
	// if($('.service__salons .accordion.selected').text() === "BeautyCity Пушкинская  ул. Пушкинская, д. 78А") {
	// }


	$(document).on('click', '.service__masters .accordion__block', function(e) {
		let clone = $(this).clone()
		console.log(clone)
		$(this).parent().parent().find('> button.active').html(clone)
	})

	// $('.accordion__block_item').click(function(e) {
	// 	const thisName = $(this).find('.accordion__block_item_intro').text()
	// 	const thisAddress = $(this).find('.accordion__block_item_address').text()
	// 	console.log($(this).parent().parent().parent().parent())
	// 	$(this).parent().parent().parent().parent().find('button.active').addClass('selected').text(thisName + '  ' +thisAddress)
	// })



	// $('.accordion__block_item').click(function(e) {
	// 	const thisChildName = $(this).text()
	// 	console.log(thisChildName)
	// 	console.log($(this).parent().parent().parent())
	// 	$(this).parent().parent().parent().parent().parent().find('button.active').addClass('selected').text(thisChildName)

	// })
	// $('.accordion.selected').click(function() {
	// 	$(this).parent().find('.panel').hasClass('selected') ?
	// 	 $(this).parent().find('.panel').removeClass('selected')
	// 		:
	// 	$(this).parent().find('.panel').addClass('selected')
	// })


	//popup
	$('.header__block_auth').click(function(e) {
		e.preventDefault()
		$('#authModal').arcticmodal();
		// $('#confirmModal').arcticmodal();

	})

	$('.rewiewPopupOpen').click(function(e) {
		e.preventDefault()
		$('#reviewModal').arcticmodal();
	})
	$('.payPopupOpen').click(function(e) {
		e.preventDefault()
		$('#paymentModal').arcticmodal();
	})
	$('.tipsPopupOpen').click(function(e) {
		e.preventDefault()
		$('#tipsModal').arcticmodal();
	})

	$('.authPopup__form').submit(function() {
		$('#confirmModal').arcticmodal();
		return false
	})

	//service
	$('.time__items .time__elems_elem .time__elems_btn').click(function(e) {
		e.preventDefault()
		$('.time__elems_btn').removeClass('active')
		$(this).addClass('active')
		// $(this).hasClass('active') ? $(this).removeClass('active') : $(this).addClass('active')
	})

	$(document).on('click', '.servicePage', function() {
		if($('.time__items .time__elems_elem .time__elems_btn').hasClass('active') && $('.service__form_block > button').hasClass('selected')) {
			$('.time__btns_next').addClass('active')
		}
	})

// Получение элементов страницы
const datepicker = document.getElementById('datepickerHere');
const timeElems = document.querySelector('.time__elems');

// Обработчик изменения выбранной даты
datepicker.addEventListener('click', function(e) {
  // Проверка, что клик был на ячейке с датой
  if (e.target.classList.contains('air-datepicker-cell')) {
    // Получение выбранной даты
    const selectedDate = e.target.dataset.date;

    // Отправка AJAX-запроса на сервер
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_free_time/?date=' + selectedDate, true);
    xhr.onload = function() {
      if (xhr.status === 200) {
        // Обработка ответа сервера
        const response = JSON.parse(xhr.responseText);
        displayFreeTime(response);
      }
    };
    xhr.send();
  }
});

function displayFreeTime(freeTimeList) {
  // Очистка предыдущего списка времени
  while (timeElems.firstChild) {
    timeElems.firstChild.remove();
  }

  const timeIntervals = Object.keys(freeTimeList);

  timeIntervals.forEach(function(interval) {
    const timeItem = document.createElement('div');
    timeItem.classList.add('time__items');

    const timeIntro = document.createElement('div');
    timeIntro.classList.add('time__elems_intro');
    timeIntro.textContent = interval;
    timeItem.appendChild(timeIntro);

    const timeElem = document.createElement('div');
    timeElem.classList.add('time__elems_elem', 'fic');

    freeTimeList[interval].forEach(function(time) {
      const button = document.createElement('button');
      button.classList.add('time__elems_btn');
      button.dataset.time = time;
      button.textContent = time;
      timeElem.appendChild(button);
    });

    timeItem.appendChild(timeElem);
    timeElems.appendChild(timeItem);
  });

  // Вызов обработчика .servicePage
  $('.servicePage').click();
}


})
