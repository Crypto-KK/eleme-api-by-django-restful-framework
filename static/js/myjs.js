$(document).ready(function () {
    api_url = 'v1/entries/';

    var csrftoken = Cookies.get('csrftoken');
    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend:function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $('#searchbtn').click(function () {
        var content = $("#search").val();
        $('#ele-table-body').empty();
        $.ajax({
            method: 'GET',
            url:api_url + '?search=' + content,
            dataType: 'json',
            success:function (data) {
                api_url = data['next'];
                if (api_url == null){
                    $('#load-more').val('已加载全部');
                    $('#load-more').attr('disabled',true);
                    api_url = 'v1/entries/';
                }
                var results = data['results'];
                for (i=0;i<results.length;i++){
                    $('#ele-table-body').append(
                        '        <tr>\n' +
                        '            <th scope="col">'+results[i]['pk']+'</th>\n' +
                        '            <th scope="col">'+results[i]['city']+'</th>\n' +
                        '            <th scope="col"><a href="/detail/' + results[i]['pk'] +'">' + results[i]['name'] + '</a></th>\n' +
                        '            <th scope="col">'+results[i]['school']+'</th>\n' +
                        '            <th scope="col">'+results[i]['score']+'</th>\n' +
                        '        </tr>'
                    )
                }
            }
        })
    });

    $('#load-more').click(function () {
        $.ajax({
            method:'GET',
            url:api_url,
            dataType:'json',
            success:function (data) {
                api_url = data['next'];
                if (api_url == null){
                    $('#load-more').val('已加载全部');
                    $('#load-more').attr('disabled',true);
                    api_url = 'v1/entries/';
                }
                var results = data['results'];
                for (i=0;i<results.length;i++){
                    $('#ele-table-body').append(
                        '        <tr>\n' +
                        '            <th scope="col">'+results[i]['pk']+'</th>\n' +
                        '            <th scope="col">'+results[i]['city']+'</th>\n' +
                        '            <th scope="col"><a href="/detail/' + results[i]['pk'] +'">' + results[i]['name'] + '</a></th>\n' +
                        '            <th scope="col">'+results[i]['school']+'</th>\n' +
                        '            <th scope="col">'+results[i]['score']+'</th>\n' +
                        '        </tr>'
                    )
                }

            }
        })
    });

    $('#loginbtn').click(function () {
        $.ajax({
            cache:false,
            type:"POST",
            url: "/login/",
            dataType: "json",
            success:function (data) {
                if (data.status=='success'){
                    location.reload();
                } else if (data.status=='fail'){
                    console.log('登录失败')
                }
            }
        })
    });

    $('#logoutbtn').click(function () {
        $.ajax({
            cache: false,
            type: 'POST',
            url:'/logout/',
            dataType:'json',
            success:function (data) {
                if (data.status=='success'){
                    location.reload()
                }
            }
        })
    });

    $('#editbtn').click(function () {
         $('#editbox').show();
    });

    $('#edit-confirm-btn').click(function () {
        var name = $('#name').val();
        var distance = $('#distance').val();
        var adderss = $('#address').val();
        var time = $('#time').val();
        var score = $('#score').val();
        var comments = $('#comments').val();
        var sell = $('#sell').val();
        var pk = $('#pk').val();
        $.ajax({
            type:'PATCH',
            url:'/detail/' + pk,
            data:{
                "name": name,
                "distance": distance,
                "address": adderss,
                "time": time,
                "score": score,
                "comments": comments,
                "sell": sell,
            },

            success:function (data) {
                if (data.status == 'ok'){
                    console.log('success');
                    location.reload();
                }
            }
        })
    })


});