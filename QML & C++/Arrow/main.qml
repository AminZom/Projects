import QtQuick 2.12

Rectangle {
    id: background
    width: 650
    height: 320
    visible: true
    color: "gray"
    Rectangle {
        id: rect
        color: "white"
        width: 300
        height: 300
        anchors {
            left: background.left
            top: background.top
            leftMargin: 10
            topMargin: 10
        }
        Image {
            id: arrow
            x: rect.width / 2 - 25; y: rect.height - 45;
            width: sourceSize.width/20; height: sourceSize.height/20
            source: "assets/arrowPic2.png";
        }
    }
    Text {
        x: 402; y: 10;
        font.pointSize: 30
        text: qsTr("Controls")
    }
    Image {
        x: 400; y: 60;
        width: sourceSize.width/8; height: sourceSize.height/8;
        source: "assets/arrowPic.png";
        MouseArea {
            anchors.fill: parent
            onClicked: {
                arrow.y = arrow.y - 10
                arrow.rotation = 0
            }
        }
    }
    Image {
        x: 500; y: 140;
        width: sourceSize.width/8; height: sourceSize.height/8;
        source: "assets/arrowPic.png";
        rotation: 90
        MouseArea {
            anchors.fill: parent
            onClicked: {
                arrow.x = arrow.x + 10
                arrow.rotation = 90
            }
        }
    }
    Image {
        x: 300; y: 140;
        width: sourceSize.width/8; height: sourceSize.height/8;
        source: "assets/arrowPic.png";
        rotation: -90
        MouseArea {
            anchors.fill: parent
            onClicked: {
                arrow.x = arrow.x - 10
                arrow.rotation = -90
            }
        }
    }
    Image {
        x: 400; y: 220;
        width: sourceSize.width/8; height: sourceSize.height/8;
        source: "assets/arrowPic.png";
        rotation: 180
        MouseArea {
            anchors.fill: parent
            onClicked: {
                arrow.y = arrow.y + 10
                arrow.rotation = 180
            }
        }
    }
}


