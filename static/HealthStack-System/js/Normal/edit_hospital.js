/*
Author       : Dreamguys
Template Name: Doccure - Bootstrap Template
Version      : 1.0
*/

(function($) {
    "use strict";
	
	// Departments Add More
	
    $(".department-info").on('click','.trash', function () {
		$(this).closest('.department-cont').remove();
		return false;
    });

    $(".add-department").on('click', function () {

        var departmentcontent = '<div class="row form-row department-cont">' +
			'<div class="col-12 col-md-8 col-lg-11">' +
				'<div class="form-group">' +

					'<label>Add New Departments</label>' +

					'<input type="text" name="department" class="form-control">' +
				'</div>' +
			'</div>' +
			'<div class="col-md-2 col-lg-1">' +
				'<label class="d-md-block d-sm-none d-none">&nbsp;</label>' +
				'<a href="#" class="btn btn-danger trash"><i class="far fa-trash-alt"></i></a>' +
			'</div>' +
		'</div>';
		
        $(".department-info").append(departmentcontent);
        return false;
    });

	// Service Add More
	
    $(".service-info").on('click','.trash', function () {
		$(this).closest('.service-cont').remove();
		return false;
    });

    $(".add-service").on('click', function () {

        var servicecontent = '<div class="row form-row service-cont">' +
			'<div class="col-12 col-md-8 col-lg-11">' +
				'<div class="form-group">' +

					'<label>Add New Services</label>' +

					'<input type="text" name="service" class="form-control">' +
				'</div>' +
			'</div>' +
			'<div class="col-md-2 col-lg-1">' +
				'<label class="d-md-block d-sm-none d-none">&nbsp;</label>' +
				'<a href="#" class="btn btn-danger trash"><i class="far fa-trash-alt"></i></a>' +
			'</div>' +
		'</div>';
		
        $(".service-info").append(servicecontent);
        return false;
    });

	// Specialization Add More
	
    $(".specialization-info").on('click','.trash', function () {
		$(this).closest('.specialization-cont').remove();
		return false;
    });

    $(".add-specialization").on('click', function () {

        var specializationcontent = '<div class="row form-row specialization-cont">' +
			'<div class="col-12 col-md-8 col-lg-11">' +
				'<div class="form-group">' +

					'<label>Add New Specializations</label>' +

					'<input type="text" name="specialization" class="form-control">' +
				'</div>' +
			'</div>' +
			'<div class="col-md-2 col-lg-1">' +
				'<label class="d-md-block d-sm-none d-none">&nbsp;</label>' +
				'<a href="#" class="btn btn-danger trash"><i class="far fa-trash-alt"></i></a>' +
			'</div>' +
		'</div>';
		
        $(".specialization-info").append(specializationcontent);
        return false;
    });
	
	// Registration Add More
	
    $(".registrations-info").on('click','.trash', function () {
		$(this).closest('.reg-cont').remove();
		return false;
    });

    $(".add-reg").on('click', function () {

        var regcontent = '<div class="row form-row reg-cont">' +
			'<div class="col-12 col-md-5">' +
				'<div class="form-group">' +
					'<label>Registrations</label>' +
					'<input type="text" class="form-control">' +
				'</div>' +
			'</div>' +
			'<div class="col-12 col-md-5">' +
				'<div class="form-group">' +
					'<label>Year</label>' +
					'<input type="text" class="form-control">' +
				'</div>' +
			'</div>' +
			'<div class="col-12 col-md-2">' +
				'<label class="d-md-block d-sm-none d-none">&nbsp;</label>' +
				'<a href="#" class="btn btn-danger trash"><i class="far fa-trash-alt"></i></a>' +
			'</div>' +
		'</div>';
		
        $(".registrations-info").append(regcontent);
        return false;
    });
	
})(jQuery);