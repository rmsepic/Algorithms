.text
	.global _start
_start
	movel	$2,%ebx
	movel	$1,%eax
	int	$0x80
