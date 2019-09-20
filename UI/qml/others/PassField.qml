import QtQuick 2.10
import QtQuick.Controls 2.3

TextField {
    color: "white"

    property string hiddenText: ""

    background: Rectangle {
        implicitWidth: 214
        implicitHeight: 28
        color: "transparent"
        border.color: Qt.rgba(255, 255, 255, 0.2)
        radius: 3
    }

    Keys.onPressed: {
        if(event.key === Qt.Key_Backspace) {
            if(text.length == 1) {
                text = ''
                hiddenText = text
            }

            text = text.substring(0, text.length-1)
            event.accepted = true
            return
        } else if(event.key === Qt.Key_Tab) {
            return
        }

        if(event.text) {
            text += "*"
            hiddenText = text
            event.accepted = true
        }

    }
}
