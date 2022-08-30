package com.sonatype.test

import com.sonatype.test.errors.foo
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class TestApplication

fun main(args: Array<String>) {
	// adding a comment
	runApplication<TestApplication>(*args)
}
