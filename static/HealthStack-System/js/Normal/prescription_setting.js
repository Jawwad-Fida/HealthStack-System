/*
Author       : Dreamguys
Template Name: Doccure - Bootstrap Template
Version      : 1.0
*/

(function($) {
    "use strict";

	// medicine Add More
	
    $(".medicine-info").on('click','.trash', function () {
		$(this).closest('.medicine-cont').remove();
		return false;
    });

    $(".add-medicine").on('click', function () {  
		
		var medicinecontent = '<div class="row form-row specimen-cont">' +
			'<div class="col-12 col-md-10 col-lg-11">' +
				'<div class="row form-row">' +
					'<div class="col-12 col-md-6 col-lg-3">' +
						'<div class="form-group">' +
							'<label>Specimen Type</label>' +
							'<input type="text" name="specimen_type" class="form-control">' +
						'</div>' +
					'</div>' +
					'<div class="col-12 col-md-6 col-lg-3">' +
						'<div class="form-group">' +
							'<label>Collection Date</label>' +
							'<input type="date" name="collection_date" class="form-control">' +
						'</div>' +
					'</div>' +
                    '<div class="col-12 col-md-6 col-lg-3">' +
						'<div class="form-group">' +
							'<label>Receiving Date</label>' +
							'<input type="date" name="receiving_date" class="form-control">' +
						'</div>' +
					'</div>' +
				'</div>' +
			'</div>' +
			'<div class="col-12 col-md-2 col-lg-1"><label class="d-md-block d-sm-none d-none">&nbsp;</label><a href="#" class="btn btn-danger trash"><i class="far fa-trash-alt"></i></a></div>' +
		'</div>';
		
        $(".medicine-info").append(medicinecontent);
        return false;
    });		

		
})(jQuery);