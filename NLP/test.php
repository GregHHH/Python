<?php declare(strict_types=1);

final class Regex
{
    /**
     * Provide a pattern to ensure the tested string contains the substring 'toto'
     */
    public static function ex1(): string
    {
        //todo: replace '//' below with your regular expression
        return '/toto/';
    }

    /**
     * Provide a pattern to ensure the tested string starts with the letter 'a'
     */
    public static function ex2(): string
    {
        return '/^a/';
    }

    /**
     * Provide a pattern to ensure the tested string contains a vowel
     */
    public static function ex3(): string
    {
        return '/[aeiouy]/';
    }

    /**
     * Provide a pattern to ensure the tested ends with 4, 5 or 6
     */
    public static function ex4(): string
    {
        return '/[456]$/';
    }

    /**
     * Provide a pattern to ensure the tested string corresponds to an integer
     */
    public static function ex5(): string
    {
        return '/-?^[0-9]+$/';
    }

    /**
     * Provide a pattern to ensure the tested string is a 4-letter *word*
     * starting with a, ending with d, without accents and special characters
     */
    public static function ex6(): string
    {
        
        return '/^a[a-zA-Z]{2}d$/';
    }

    /**
     * Provide a pattern to ensure the tested string is actually an even positive integer
     */
    public static function ex7(): string
    {
        return '/^\d*[02468]$/';
    }

    /**
     * Provide a pattern to ensure the tested string is a number, eg. '2' or '-253.24'
     */
    public static function ex8(): string
    {
         return '/-?\d*(?:\.?\d*)\d$/';
    }

    /**
     * Provide a pattern to ensure the tested string starts with the letter 'A' or 'a'
     */
    public static function ex9(): string
    {
        return '/^[a A]/';
    }

	/**
     * Provide a pattern to ensure the tested string is a properly formatted number, eg. '2', '-253.24' or '23,253,326.35'
     */
    public static function ex10(): string
    {
        return '/-?(?:\d*\,{1}?)*\d*(?:\.?\d*)\d$/';
    }
}
