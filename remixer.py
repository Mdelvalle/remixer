from pydub import AudioSegment as audio


class Remixer(object):
    def __init__(self, songs, dur):
        assert songs

        print 'Initializing songs...'
        print ''

        self.songs = [audio.from_mp3(song) for song in songs]

        # Percentage of song that will be used
        self.dur = dur or 100
        print 'PERCENTAGE: %d' % self.dur


    def song_section(self, song):
        import random

        song_dur = len(song)
        print 'SONG DURATION: %d' % song_dur

        # Duration of new song
        song_perc = (song_dur * self.dur) / 100
        print 'NEW DURATION: %d' % song_perc

        # Get new start and ending positions of song
        start = random.randint(0, song_perc)
        print 'START: %d' % start

        end = start + song_perc
        print 'END: %d' % end

        print 'DIFFERENCE: %d' % (end - start)
        print ''

        assert (end - start) == song_perc

        return (start, end)


    def remix(self):
        playlist = audio.empty()
        for song in self.songs:
            (start, end) = self.song_section(song)
            new_song = song[start:end]
            print len(new_song)

            print 'concatenating song...'
            playlist += new_song

            # playlist.append(new_song, crossfade=5000)

        print 'LENGTH OF FINAL SONG: %d' % len(playlist)
        print ''
        print 'fading out...'
        print ''
        playlist = playlist.fade_out(10)


        print 'exporting...'
        print ''
        playlist.export('1337MIX.mp3', format='mp3')


def main():
    """
    Parses user input for songs and an optional duration.
    Creates and calls the Remixer class.
    """
    import argparse

    parser = argparse.ArgumentParser(usage='remixer.py [songs] [-dur]')
    parser.add_argument('songs', nargs='+')
    parser.add_argument('-dur', type=int)
    args = vars(parser.parse_args())

    if 'dur' in args:
        remixer = Remixer(args['songs'], args['dur'])
    else:
        remixer = Remixer(args['songs'])

    remixer.remix()


if __name__ == '__main__':
    main()
