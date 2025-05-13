function initMap() {
    const ncuLocation = { lat: 24.9685, lng: 121.1919 };

    // 建立地圖
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 16,
        center: ncuLocation
    });

    // 加上中央大學標記
    new google.maps.Marker({
        position: ncuLocation,
        map: map,
        title: "中央大學",
        icon: {
            url: "http://maps.google.com/mapfiles/ms/icons/red-dot.png"
        }
    });

    // 拿掉 loading 畫面
    document.getElementById('loading').style.display = 'none';

    // 定位使用者
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const userLocation = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude
                };

                new google.maps.Marker({
                    position: userLocation,
                    map: map,
                    title: "你在這裡！",
                    icon: {
                        url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
                    }
                });

                map.setCenter(userLocation);

                alert("定位成功！已經移動到你的所在地。");
            },
            (error) => {
                console.error("定位失敗：", error);
                alert("定位失敗，顯示中央大學地圖。");
            }
        );
    } else {
        console.error("這個瀏覽器不支援定位");
        alert("你的瀏覽器不支援定位功能。");
    }
}
