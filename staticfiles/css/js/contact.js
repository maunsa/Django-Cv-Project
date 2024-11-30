$(document).ready(function () {

    (function ($) {
        "use strict";


        jQuery.validator.addMethod('answercheck', function (value, element) {
            return this.optional(element) || /^\bcat\b$/.test(value)
        }, "type the correct answer -_-");

        // validate contactForm form
        $(function () {
            $('#contactForm').validate({
                rules: {
                    name: {
                        required: true,
                        minlength: 2
                    },
                    subject: {
                        required: true,
                        minlength: 4
                    },
                    number: {
                        required: true,
                        minlength: 5
                    },
                    email: {
                        required: true,
                        email: true
                    },
                    message: {
                        required: true,
                        minlength: 20
                    }
                },
                messages: {
                    name: {
                        required: "come on, you have a name, don't you?",
                        minlength: "your name must consist of at least 2 characters"
                    },
                    subject: {
                        required: "come on, you have a subject, don't you?",
                        minlength: "your subject must consist of at least 4 characters"
                    },
                    number: {
                        required: "come on, you have a number, don't you?",
                        minlength: "your Number must consist of at least 5 characters"
                    },
                    email: {
                        required: "no email, no message"
                    },
                    message: {
                        required: "um...yea, you have to write something to send this form.",
                        minlength: "thats all? really?"
                    }
                },
                submitHandler: function (form1) {
                    console.log("Submit handler çalışıyor."); // Bu mesaj konsolda görünmeli
                    $(form1).ajaxSubmit({
                        type: "POST",
                        data: $(form1).serialize(),
                        url: "/contact/contact_form",
                        success: function (response) {
                            console.log(response);
                            if (response.success) {
                                $('#contactForm :input').attr('disabled', 'disabled');
                                $('#contactForm').fadeTo("slow", 1, function () {
                                    $(this).find(':input').attr('disabled', 'disabled');
                                    $(this).find('label').css('cursor', 'default');
                                    $('.modal').modal('hide'); // Diğer açık modalları kapat
                                    $('#success').modal('show'); // Başarı modalını göster
                                });
                            } else {
                                $('#contactForm').fadeTo("slow", 1, function () {
                                    $('.modal').modal('hide'); // Diğer açık modalları kapat
                                    $('#error').modal('show'); // Hata modalını göster
                                });

                            }
                        },
                        error: function () {
                            $('#contactForm').fadeTo("slow", 1, function () {
                                $('.modal').modal('hide'); // Diğer açık modalları kapat
                                $('#error').modal('show'); // Hata modalını göster
                            });
                        }
                    });
                }

            })
        })

    })(jQuery)
})