// Problem Link: 
// https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/javascript

function songDecoder(song){
  // ...
  while(song.indexOf('WUB') != -1)
    {
      song = song.replace('WUB', ' ')
      song = song.replace('  ', ' ')
      
    }
  return song.trim()
}


console.log(songDecoder('WUBWUBAmaroWUBWUBporanoWUBjahaWUBWUBchaay'))