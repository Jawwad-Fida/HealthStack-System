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
							'<label>Specimen ID</label>' +
							'<input type="text" name="specimen_ID" class="form-control">' +
						'</div>' +
					'</div>' +
					'<div class="col-12 col-md-6 col-lg-4">' +
						'<div class="form-group">' +
							'<label>Specimen Type</label>' +
							'<input type="text" name="specimen_type" class="form-control">' +
						'</div>' +
					'</div>' +
					'<div class="col-12 col-md-6 col-lg-4">' +
						'<div class="form-group">' +
							'<label>Collection Date/Time</label>' +
							'<input type="text" name="collection_date" class="form-control">' +
						'</div>' +
					'</div>' +
                    '<div class="col-12 col-md-6 col-lg-4">' +
						'<div class="form-group">' +
							'<label>Receiving Date/Time</label>' +
							'<input type="text" name="receiving_date" class="form-control">' +
						'</div>' +
					'</div>' +
				'</div>' +
			'</div>' +
			'<div class="col-12 col-md-2 col-lg-1"><label class="d-md-block d-sm-none d-none">&nbsp;</label><a href="#" class="btn btn-danger trash"><i class="far fa-trash-alt"></i></a></div>' +
		'</div>';
		
        $(".specimen-info").append(specimencontent);
        return false;
    });		
})(jQuery);