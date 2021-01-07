// 함수 joinOptions ()가 두 개의 인수 만 지정하여 JSON 형식 (예 : "[a, b, c]")으로 목록을 반환하도록합니다.

fun joinOptions(options: Collection<String>) =
        options.joinToString(prefix = "[", postfix = "]")
