<script lang="ts">
  import "$lib/app.css";
  import Error from '$lib/error.svelte';
  import MapDashboard from './map_dashboard.svelte';

  import LoadingSnake from '$lib/loading_snake.svelte';

  export let data;
</script>

{#await data.discovered}
  <LoadingSnake />
{:then discovered}
  {#if discovered}
     <MapDashboard ip={data.ip} port={data.port}/>
  {:else}
    <Error path="/" message="unable to discover {data.ip} : {data.port}"/>
  {/if}
{:catch error}
  <Error path="/" message={error.message}/>
{/await}
