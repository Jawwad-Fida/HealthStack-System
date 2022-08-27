function search() {
    var name = document.getElementById("searchForm").elements["searchItem"].value;
    var pattern = name.toLowerCase();
    var targetId = "";
  
    var divs = document.getElementsByClassName("col-md-2");
    for (var i = 0; i < divs.length; i++) {
      var para = divs[i].getElementsByTagName("p");
      var index = para[0].innerText.toLowerCase().indexOf(pattern);
      if (index != -1) {
        targetId = divs[i].parentNode.id;
        document.getElementById(targetId).scrollIntoView();
        break;
      }
    }
  }
  