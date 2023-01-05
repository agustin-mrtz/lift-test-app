package com.sonatype.test.errors

import java.io.IOException

class Foo {

    override fun toString(): String {
        throw IllegalStateException() // exception should not be thrown here
    }

}

fun foo(bar: Int) {
    if (bar < 1) {
        throw Exception() // too generic exception thrown here
    }
    // ...
}
