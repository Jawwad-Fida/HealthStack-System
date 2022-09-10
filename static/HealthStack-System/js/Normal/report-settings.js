/*
Author       : Dreamguys
Template Name: Doccure - Bootstrap Template
Version      : 1.0
*/

(function($) {
    "use strict";

	// Specimen Add More
	
    $(".specimen-info").on('click','.trash', function () {
		$(this).closest('.specimen-cont').remove();
		return false;
    });

    $(".add-specimen").on('click', function () {  
		
		var specimencontent = '<div class="row form-row specimen-cont">' +
			'<div class="col-12 col-md-10 col-lg-11">' +
				'<div class="row form-row">' +
					'<div class="col-12 col-md-6 col-lg-4">' +
						'<div class="form-group">' +
							'<label>Specimen Type</label>' +
							'<input type="text" name="specimen_type" class="form-control">' +
						'</div>' +
					'</div>' +
					'<div class="col-12 col-md-6 col-lg-4">' +
						'<div class="form-group">' +
							'<label>Collection Date</label>' +
							'<input type="date" name="collection_date" class="form-control">' +
						'</div>' +
					'</div>' +
                    '<div class="col-12 col-md-6 col-lg-4">' +
						'<div class="form-group">' +
							'<label>Receiving Date</label>' +
							'<input type="date" name="receiving_date" class="form-control">' +
						'</div>' +
					'</div>' +
				'</div>' +
			'</div>' +
			'<div class="col-12 col-md-2 col-lg-1"><label class="d-md-block d-sm-none d-none">&nbsp;</label><a href="#" class="btn btn-danger trash"><i class="far fa-trash-alt"></i></a></div>' +
		'</div>';
		
        $(".specimen-info").append(specimencontent);
        return false;
    });		

	// Test Add More
	
    $(".test-info").on('click','.trash', function () {
		$(this).closest('.test-cont').remove();
		return false;
    });

    $(".add-test").on('click', function () {  
		
		var testcontent = '<div class="row form-row test-cont">' +
			'<div class="col-12 col-md-10 col-lg-11">' +
				'<div class="row form-row">' +
					'<div class="col-12 col-md-6 col-lg-3">' +
						'<div class="form-group">' +
							'<label>Test Name</label>' +
							'<input type="text" name="test_name" class="form-control">' +
						'</div>' +
					'</div>' +
					'<div class="col-12 col-md-6 col-lg-3">' +
						'<div class="form-group">' +
							'<label>Result</label>' +
							'<input type="text" name="result" class="form-control">' +
						'</div>' +
					'</div>' +
					'<div class="col-12 col-md-6 col-lg-3">' +
						'<div class="form-group">' +
							'<label>Unit</label>' +
							'<input type="text" name="unit" class="form-control">' +
						'</div>' +
					'</div>' +
                    '<div class="col-12 col-md-6 col-lg-3">' +
						'<div class="form-group">' +
							'<label>Referred Value</label>' +
							'<input type="text" name="referred_value" class="form-control">' +
						'</div>' +
					'</div>' +
				'</div>' +
			'</div>' +
			'<div class="col-12 col-md-2 col-lg-1"><label class="d-md-block d-sm-none d-none">&nbsp;</label><a href="#" class="btn btn-danger trash"><i class="far fa-trash-alt"></i></a></div>' +
		'</div>';
		
        $(".test-info").append(testcontent);
        return false;
    });		
})(jQuery);