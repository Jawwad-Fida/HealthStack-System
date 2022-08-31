var loader_script = '<div id="pre-loader">' +
    '<div class="spinner-border text-primary" role="status">' +
    '<span class="sr-only">Loading...</span>' +
    '</div>' +
    '</div>';
window.start_loader = function() {
    if ($('body>#pre-loader').length <= 0) {
        $('body').append(loader_script)
    }
}
window.end_loader = function() {
    var loader = $('body>#pre-loader')
    if (loader.length > 0) {
        loader.remove()
    }
}